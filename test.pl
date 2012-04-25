#! /opt/local/bin/perl
use warnings;
use strict;
#@lines=`perldoc -u -f atan2`;
#foreach(@lines){
#    s/\w<([^>]+)/\U$1/g;
#    print;
#}
my $n = 1;
sub marine{
    my($max_so_far) = pop @_;
    foreach(@_){
        if($_>$max_so_far){
            $max_so_far = $_;
        }
    }
    $max_so_far;
};
print &marine(1,2,3,4,2,10);
