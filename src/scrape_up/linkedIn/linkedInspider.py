import scrapy


class LinkedInPeopleProfileSpider(scrapy.Spider):
    name = "linkedin_people_profile"
    custom_settings = {
        'FEEDS': {'data/%(name)s_%(time)s.jsonl': {'format': 'jsonlines',}}
    }

    def start_requests(self):
        profile_list = ['reidhoffman']  # Any public profile username can be added
        for profile in profile_list:
            linkedin_people_url = f'https://www.linkedin.com/in/{profile}/'
            yield scrapy.Request(url=linkedin_people_url, callback=self.parse_profile,
                                 meta={'profile': profile, 'linkedin_url': linkedin_people_url})

    def parse_profile(self, response):
        item = LinkedInProfileItem()
        item['profile'] = response.meta['profile']
        item['url'] = response.meta['linkedin_url']

        summary_box = response.css("section.top-card-layout")
        item['name'] = summary_box.css("h1::text").get().strip()
        item['description'] = summary_box.css("h2::text").get().strip()

        location_info = summary_box.css('div.top-card__subline-item::text').get()
        if location_info:
            item['location'] = location_info.strip()
        else:
            item['location'] = ''

        item['followers'] = ''
        item['connections'] = ''

        for span_text in summary_box.css('span.top-card__subline-item::text').getall():
            if 'followers' in span_text:
                item['followers'] = span_text.replace(' followers', '').strip()
            if 'connections' in span_text:
                item['connections'] = span_text.replace(' connections', '').strip()

        about_section = AboutSection(response)
        item['about'] = about_section.extract_about()

        experience_section = ExperienceSection(response)
        item['experience'] = experience_section.extract_experience()

        education_section = EducationSection(response)
        item['education'] = education_section.extract_education()

        yield item


class AboutSection:
    def __init__(self, response):
        self.response = response

    def extract_about(self):
        about = self.response.css('section.summary div.core-section-container__content p::text').get(default='')
        return about


class ExperienceSection:
    def __init__(self, response):
        self.response = response

    def extract_experience(self):
        experience_list = []
        experience_blocks = self.response.css('li.experience-item')

        for block in experience_blocks:
            experience = {}
            experience['organisation_profile'] = block.css('h4 a::attr(href)').get(default='').split('?')[0]
            experience['location'] = block.css('p.experience-item__location::text').get(default='').strip()

            try:
                experience['description'] = block.css('p.show-more-less-text__text--more::text').get().strip()
            except Exception as e:
                print('experience --> description', e)
                try:
                    experience['description'] = block.css('p.show-more-less-text__text--less::text').get().strip()
                except Exception as e:
                    print('experience --> description', e)
                    experience['description'] = ''

            try:
                date_ranges = block.css('span.date-range time::text').getall()
                if len(date_ranges) == 2:
                    experience['start_time'] = date_ranges[0]
                    experience['end_time'] = date_ranges[1]
                    experience['duration'] = block.css('span.date-range__duration::text').get()
                elif len(date_ranges) == 1:
                    experience['start_time'] = date_ranges[0]
                    experience['end_time'] = 'present'
                    experience['duration'] = block.css('span.date-range__duration::text').get()
            except Exception as e:
                print('experience --> time ranges', e)
                experience['start_time'] = ''
                experience['end_time'] = ''
                experience['duration'] = ''

            experience_list.append(experience)

        return experience_list


class EducationSection:
    def __init__(self, response):
        self.response = response

    def extract_education(self):
        education_list = []
        education_blocks = self.response.css('li.education__list-item')

        for block in education_blocks:
            education = {}
            education['organisation'] = block.css('h3::text').get(default='').strip()
            education['organisation_profile'] = block.css('a::attr(href)').get(default='').split('?')[0]

            try:
                course_details = ''
                for text in block.css('h4 span::text').getall():
                    course_details = course_details + text.strip() + ' '
                education['course_details'] = course_details.strip()
            except Exception as e:
                print("education --> course_details", e)
                education['course_details'] = ''

            education['description'] = block.css('div.education__item--details p::text').get(default='').strip()

            try:
                date_ranges = block.css('span.date-range time::text').getall()
                if len(date_ranges) == 2:
                    education['start_time'] = date_ranges[0]
                    education['end_time'] = date_ranges[1]
                elif len(date_ranges) == 1:
                    education['start_time'] = date_ranges[0]
                    education['end_time'] = 'present'
            except Exception as e:
                print("education --> time_ranges", e)
                education['start_time'] = ''
                education['end_time'] = ''

            education_list.append(education)

        return education_list


class LinkedInProfileItem(scrapy.Item):
    profile = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    location = scrapy.Field()
    followers = scrapy.Field()
    connections = scrapy.Field()
    about = scrapy.Field()
    experience = scrapy.Field()
    education = scrapy.Field()

