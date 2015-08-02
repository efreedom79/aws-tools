#!/usr/bin/python

import argparse
import boto

def tag(bucketname, tagname, tagvalue):
   bucket = conn.get_bucket(bucketname)
   tagset = boto.s3.tagging.TagSet()
   tagset.add_tag(tagname, tagvalue)
   tag = boto.s3.tagging.Tags()
   tag.add_tag_set(tagset)
   bucket.set_tags(tag)

if __name__ == "__main__":

    helptitle = "Set a tag on an S3 Bucket"
    parser = argparse.ArgumentParser(description=helptitle)
    parser.add_argument("-b", "--bucket",   help="Choose the Bucket Name that you want to add a tag to", default=None )
    parser.add_argument("-n", "--tagname",  help="Choose the Tag Name to update", default=None)
    parser.add_argument("-v", "--tagvalue", help="Enter the tag value for this tagname and bucket", default=None)

    args = parser.parse_args()

    if args.tagvalue == None or args.tagname == None or args.bucket == None:
        print "You need to provide an argument for the bucket name, the tag name and the tag value"
        exit()

    print "Bucket:    %s" % args.bucket
    print "Tag Name:  %s" % args.tagname
    print "Tag Value: %s" % args.tagvalue

    tag(args.bucket, args.tagname, args.tagvalue)

### Planned Modifications
###     Allow default for --tagname and tagvalue to be "Name" and the Bucket Name respectively
###     Only print the info when -v is set on, otherwise it's silent mode
###     Overwrite tags by default but provide flag that says Do Not Overwrite

