# instagram-web-crawler-python

## Python dependencies
```
numpy, cv2, urllib, firebase, BeautifulSoup4
```

## Crawling location-id nearby a coordinate
```
python instagram_locationid_request.py <output_type> <start_lat> <start_lng> <end_lat> <end_lng> <distance>
ex) python instagram_locationid_request.py print 37.614061 126.793019 37.479233 127.126362 100
```


## Crawling posts on a specific location-id
```
python instagram_webcrawl_by_locationid.py <output_type> <location_id> <max_id>
ex) python instagram_webcrawl_by_locationid.py print 254687352 1474635062204921374
```

## Training/testing dataset (RF, SVM, k-nearest, boost, MLP)
```
test_model_precision('dat_train_c.txt')
train('dat_train_c.txt', 'svm_model_161212.ml')
test('dat_test_c.txt', 'svm_model_161212.ml')
````

