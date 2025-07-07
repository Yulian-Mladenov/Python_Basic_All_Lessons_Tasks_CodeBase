number_of_pages_of_the_current_book = int(input())
pages_he_can_read_per_hour = int(input())
number_of_the_days_he_must_read_the_current_book = int(input())

total_time_for_read_the_current_book = number_of_pages_of_the_current_book // pages_he_can_read_per_hour

how_many_hours_need_to_read_per_day = total_time_for_read_the_current_book // number_of_the_days_he_must_read_the_current_book

print(how_many_hours_need_to_read_per_day)