#! /usr/bin/env python3

###
# KINOVA (R) KORTEX (TM)
#
# Copyright (c) 2018 Kinova inc. All rights reserved.
#
# This software may be modified and distributed under the
# terms of the BSD 3-Clause license.
#
# Refer to the LICENSE file for details.
#
###

from jaco3_armbase.autogen.client_stubs.BaseClientRpc import BaseClient
from jaco3_armbase.autogen.messages import Base_pb2


def example_manipulation_protobuf_basic():
    # In protobuf, there's many scalar value types you can declare. 
    # All those type have a coresponding type in python. 
    # Here's the list:
    
    # Proto type : Python type
    # double : float
    # float : float
    # int32 : int
    # int64 : int
    # uint32 : int/long
    # uint64 : int/long
    # sint32 : int
    # sint64 : int/long
    # fixed32 : int/long
    # fixed64 : int/long
    # sfixed32 : int
    # sfixed64 : int/long
    # bool : bool
    # string : str
    # bytes : str

    # Those type can be used like regular python variable.
    # For more information about Scalar Value Types visits:
    # https://developers.google.com/protocol-buffers/docs/proto3#scalar

    # You can regroup many of these scalar value in a message. The message is a structure used in protobuf
    # to make sure all information is scope in an object. Scalar Value can't live on their own
    # if they are not contain in a message.

    # Here's a quick example using the Kinova API UserProfile message:
    # message UserProfile {
    #     Kinova.Api.Common.UserProfileHandle handle = 1; //User handle (no need to set it with CreateUserProfile()
    #     string username = 2; // username, which is used to connect to robot (or login via Web App)
    #     string firstname = 3; //user first name
    #     string lastname = 4; //user last name
    #     string application_data = 5; //other application data (used by Web App)
    # }

    user_profile = Base_pb2.UserProfile()
    # Each scalar value in a message have a set_<field> function to set the value and a getter which is
    # simply the variable name
    user_profile.username = "jcash" # We can directly affect data to variable attribute
    user_profile.firstname = "Johnny"
    user_profile.lastname = "Cash"
    # Handle and application_data are ignore on purpose

def example_manipulation_protobuf_object():


    # One of the basics element in protobuf are the message. They are the main element in protobuf
    # just like class in python. You need a message to make workable object. A message can contain
    # many kind of element. For now, we have already covered the Scalar Value and in this section we
    # going to cover message.

    # A message can make a reference to another message to make more complete element

    # For this example I'll use the FullUserProfile and UserProfile message
    # message FullUserProfile {
    #     UserProfile user_profile = 1; //User Profile, which includes username
    #     string password = 2; //User's password
    # }
    # message UserProfile {
    #     Kinova.Api.Common.UserProfileHandle handle = 1; //User handle (no need to be set)
    #     string username = 2; // username, which is used to connect to robot (or login via Web App)
    #     string firstname = 3; //user first name
    #     string lastname = 4; //user last name
    #     string application_data = 5; //other application data (used by Web App)
    # }

    # https://developers.google.com/protocol-buffers/docs/proto3#simple

    full_user_profile = Base_pb2.FullUserProfile()
    # Now I'll put data in the scalar value
    full_user_profile.password = "MyPassword"

    # Now I want to work with the user profile attribute which is a message itself. 
    # Since user profile is a message you can use the . to get access 
    # to those attribute.
    full_user_profile.user_profile.username = "jcash"
    full_user_profile.user_profile.firstname = "Johnny"
    full_user_profile.user_profile.lastname = "Cash"

    # Another basic element is the Enum. Enum are directly available from 
    # the message no need to pass by the enum 'message'.
    # Here's a example:
    # enum LimitationType {
    #     UNSPECIFIED_LIMITATION = 0; //unspecified limitation
    #     FORCE_LIMITATION = 1; //force limitation
    #     ACCELERATION_LIMITATION = 2; //acceleration limitation
    #     VELOCITY_LIMITATION = 3; //velocity limitation
    # }

    # message LimitationTypeIdentifier { 
    #     LimitationType type = 1; //limitation type
    # }

    # https://developers.google.com/protocol-buffers/docs/proto3#enum

    limitation_type_identifier = Base_pb2.LimitationTypeIdentifier()
    limitation_type_identifier.type = Base_pb2.FORCE_LIMITATION


def example_manipulation_protobuf_list():

    # In protobuf, list are called repeated once they are affected to a python
    # variable they can be used as a normal list.

    # Take note that a repeated message field doesn't have an append() function, it has an
    # add() function that create the new message object.

    # For this example we will use those two messages
    # message Sequence {
    #     SequenceHandle handle = 1
    #     string name = 2
    #     string application_data = 3
    #     repeated SequenceTask tasks = 4
    # }

    # message SequenceTask {
    #     uint32 group_identifier = 1;
    #     Action action = 2; 
    #     string application_data = 3;
    # }

    # To keep a clearer example the attribute action in SequenceTask message will be keep to default value

    # Here's 2 way to add to a repeated message field


    # Create the parent message
    sequence = Base_pb2.Sequence()
    sequence.name = "Sequence"

    # The extend way
    sequence_task_1 = Base_pb2.SequenceTask()
    sequence_task_1.group_identifier = 10
    action = sequence_task_1.action
    action = Base_pb2.Action() # Using Action default constructor
    sequence.tasks.extend([sequence_task_1]) # Extend expect an iterable

    # Created for the add() function unique to repeated message field
    sequence_task_2 = sequence.tasks.add()
    sequence_task_2.group_identifier = 20
    action = sequence_task_2.action
    action = Base_pb2.Action() # Using Action default constructor

    # Since sequence.task is a list we can use all the python toolset to
    # loop, iterate, interogate and print element in that list
    for i in range(len(sequence.tasks)):
        print("sequence ID with index : {0}".format(sequence.tasks[i].group_identifier))


    # The list still have the iterator proprety of python list so you can directly iterate
    # throught element without creating a iterator like previous example
    for task in sequence.tasks:
        print("sequence ID with object iterator : {0}".format(task.group_identifier))


def example_manipulation_protobuf_helpers():

    # Google offers some helpers with protobuf
    # We will cover some of them in this section

    # All the module google.protobuf documentation is available here:
    # https://developers.google.com/protocol-buffers/docs/reference/python/

    # First, the function include with message instance. We will cover the next function
    #     Clear
    #     MergeFrom
    #     CopyFrom

    # The Clear function is strainght forward it clear all the message attribute.

    # MergeFrom and CopyFrom have the same purpose, To duplicate data into another object.
    # The difference between them is CopyFrom will do a Clear before a MergeFrom.
    
    # For it's part MergeFrom will merge data if the new field is not empty.
    # In case of repeated, the content receive in parameter will be append

    # For this example, I'll used the Ssid message
    # message Ssid {
    #     string identifier = 1;
    # }


    # First I'll create 4 of them with unique string
    ssid_1 = Base_pb2.Ssid()
    ssid_1.identifier = ""

    ssid_2 = Base_pb2.Ssid()
    ssid_2.identifier = "123"

    ssid_3 = Base_pb2.Ssid()
    ssid_3.identifier = "@#$"

    # Now I'll Merge ssid_1 in ssid_2 and print the identifier of ssid_2
    ssid_2.MergeFrom(ssid_1)
    print("Content ssid_2: {0}".format(ssid_2.identifier))
    # output : Content ssid_2: 123

    # Now I'll Copy ssid_1 in ssid_3 and print the identifier of ssid_3
    ssid_3.CopyFrom(ssid_1)
    print("Content ssid_3: {0}".format(ssid_3.identifier))
    # output : Content ssid_3:

    # For more function visit the Class Message documentation
    # https://developers.google.com/protocol-buffers/docs/reference/python/google.protobuf.message.Message-class

    # From the protobuf library you can used the json_format module.
    # One useful function is the MessageToJson.
    # This function serialize the protobuf message to a json object it help alot when you want to print large object in 
    # a human readable way.

    # Here's an example with the following two message
    # message Sequence {
    #     SequenceHandle handle = 1
    #     string name = 2
    #     string application_data = 3
    #     repeated SequenceTask tasks = 4
    # }

    # message SequenceTask {
    #     uint32 group_identifier = 1;
    #     Action action = 2; 
    #     string application_data = 3;
    # }

    # I quickly populate the message
    sequence = Base_pb2.Sequence()
    sequence.name = "A Name"

    for i in range(5):
        sequence_task = sequence.tasks.add()
        sequence_task.group_identifier = 10 * (i + 1) # Some further function doesn't print if value = 0
        action = sequence_task.action
        action = Base_pb2.Action() # Using Action default constructor


    # We need to import the module
    from google.protobuf import json_format
    
    # Now to get the json object
    json_object = json_format.MessageToJson(sequence)
    
    # Now you can print it
    print("Json object")
    print(json_object)
    # output:
    # Json object
    # {
    #   "name": "A Name",
    #   "tasks": [
    #     {
    #       "groupIdentifier": 10
    #     },
    #     {
    #       "groupIdentifier": 20
    #     },
    #     {
    #       "groupIdentifier": 30
    #     },
    #     {
    #       "groupIdentifier": 40
    #     },
    #     {
    #       "groupIdentifier": 50
    #     }
    #   ]
    # }


    # From the protobuf library you can used the text_format module
    # A useful function is the MessageToString. It has the same purpose of 
    # MessageToJson convert the message to a human readable format

    # For the example I'll reuse the sequence object created in previous example 

    # First import the module
    from google.protobuf import text_format

    # Now print
    print("Text format")
    print(text_format.MessageToString(sequence))
    # output:
    # Text format
    # name: "A Name"
    # tasks {
    #   group_identifier: 10
    # }
    # tasks {
    #   group_identifier: 20
    # }
    # tasks {
    #   group_identifier: 30
    # }
    # tasks {
    #   group_identifier: 40
    # }
    # tasks {
    #   group_identifier: 50
    # }


if __name__ == "__main__":
    example_manipulation_protobuf_basic()
    example_manipulation_protobuf_object()
    example_manipulation_protobuf_list()
    example_manipulation_protobuf_helpers()