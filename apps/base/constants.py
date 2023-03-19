from rangefilter.filters import DateRangeFilter

# Date filterus used for admin setup
date_filters = (('created_at', DateRangeFilter),
                ('modified_at', DateRangeFilter),)