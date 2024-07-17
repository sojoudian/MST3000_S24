app_service_uptime = 99.95 / 100
azure_ad_b2c_uptime = 99.99 / 100
application_gateway_uptime = 99.95 / 100
azure_sql_gatabase_uptime = 99.995 /100

#App Service % uptime X Azure AD B2C % uptime X Azure Application Gateway % uptime X Azure SQL Database % uptime = Total % Uptime

total_uptime = app_service_uptime * azure_ad_b2c_uptime * azure_sql_gatabase_uptime * application_gateway_uptime
print(total_uptime)

# Calculate the total uptime percentage
total_uptime_percentage = total_uptime * 100
print(total_uptime_percentage)

total_uptime_percentage = round(total_uptime_percentage, 4)
print(total_uptime_percentage)
