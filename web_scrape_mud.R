if(!require(pacman)) install.packages(pacman)
pacman::p_load(robotstxt, xml2, rvest, stringr)

# paths_allowed(paths = c("http://greengables-1.tripod.com/script/1part1.html"))
# TRUE

#-----------------------------------------

# following the tutorial here:
# https://www.dataquest.io/blog/web-scraping-in-r-rvest/

# and this one
# https://www.analyticsvidhya.com/blog/2017/03/beginners-guide-on-web-scraping-in-r-using-rvest-with-hands-on-knowledge/

url <- "http://greengables-1.tripod.com/script/1part1.html"

webpage <- xml2::read_html(url)
webpage

webpage %>% 
  rvest::html_nodes("font") %>% 
  rvest::html_text()

webpage %>% 
  rvest::html_nodes("td") %>% 
  rvest::html_text()

#-----------------------------------

# you on your own

temp <- webpage %>% 
  rvest::html_nodes("td") %>% 
  rvest::html_text()
temp <- temp[[12]]

temp2 <- temp %>% 
  str_split("\n") %>% 
  unlist()

kt <- temp %>% 
  str_split("\n") %>% 
  unlist() %>% 
  str_split_fixed(":",2)

kt <- temp %>% 
  str_split("\n") %>% 
  unlist() %>% 
  str_split_fixed(":",2)