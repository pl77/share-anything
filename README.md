## TODO

* Monitoring progress for file uploads
  - See [this](https://stackoverflow.com/questions/13909900/progress-of-python-requests-post).

* Multiple file uploads
  - If multiple formats then file host zip (< 1GB zip file limit)?
  - If all images then imgur album
  - If all < 1MB text files then gist collection.
  - Else file host zip (< 1GB zip file size limit?)

* Split up the common functionality between `upload_single` and `upload_multiple` into helper functions.

* Simplify imgur album upload