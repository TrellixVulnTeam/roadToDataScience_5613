import gql from 'graphql-tag'


export const CreateEmail = gql`mutation createEmail($email: String) {
    createEmail(email: $email) {
      newEmail {
               email
      }
      
    }
  }`


export  const EmailQuery = gql`
{
  emails {
    email
  }
}
`;

export const CreateMessage = gql`mutation createMessage($firstName: String, $lastName: String, $email: String, $phone: String, $message: String) {
  createMessage(firstName:$firstName, lastName:$lastName, email: $email, phone:$phone, message:$message) {
    newMessage {
             firstName,
             lastName,
             email,
             phone,
             message
    }
    
  }
}`

export  const MessageQuery = gql`
{
  messages {
    firstName,
    lastName,
    email,
    phone,
    message
  }
}
`;