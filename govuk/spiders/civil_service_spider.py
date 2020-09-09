import scrapy

class CivilServiceSpider(scrapy.Spider):
    name = "civilservice"

    # Start url
    # https://www.civilservicejobs.service.gov.uk/csr/jobs.cgi?pageaction=searchbyquick&storesearchcontext=1&nghr_job_category=166625

    def start_requests(self):
        urls = [
            'https://www.civilservicejobs.service.gov.uk/csr/jobs.cgi?pageaction=searchbyquick&storesearchcontext=1&nghr_job_category=166625'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for job in response.css('.search-results-job-box'):
            yield {
                'source_entity': 'civilservicejobs',
                'name': job.css('.search-results-job-box-title a::text').get(),
                'url': job.css('.search-results-job-box-title a::attr(src)').extract(),
                'reference': job.css('.search-results-job-box-refcode::text').get().replace("Reference: ", "")
            }