// Main module
Module main()
    // Declare input variables
    Declare String inputName, inputType
    Declare Integer inputAge

    // Create a Pet object
    Declare Pet Animal = new Pet()

    // Get values for a pet
    Display "Enter a pet name:"
    Input inputName
    Animal.setName(inputName)

    Display "Enter a pet type:"
    Input inputType
    Animal.setType(inputType)

    Display "Enter a pet age:"
    Input inputAge
    Animal.setAge(inputAge)

    // Show values for this pet
    Display "The pet name is ", Animal.getName()
    Display "The pet type is ", Animal.getType()
    Display "The pet age is ", Animal.getAge()
End Module


// Class Pet
Class Pet
    // Fields
    Private String name
    Private String type
    Private Integer age

    // Constructor
    Public Module Pet()
        // Empty constructor
    End Module

    // Mutators
    Public Module setName(String n)
        Set name = n
    End Module

    Public Module setType(String t)
        Set type = t
    End Module

    Public Module setAge(Integer a)
        Set age = a
    End Module

    // Accessors
    Public Function String getName()
        Return name
    End Function

    Public Function String getType()
        Return type
    End Function

    Public Function getAge()
        Return age
    End Function
End Class
