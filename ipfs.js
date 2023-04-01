// const verbwire = require('verbwire')('sk_live_c07f6ba3-d6fc-4882-a833-51f7f7f6898d');

def upload_file(filePath):
    const sdk = require('api')('@verbwire/v1.0#4psk2mplfwliyql');

    let filePath = 'feel forte.png'
    sdk.auth('sk_live_c07f6ba3-d6fc-4882-a833-51f7f7f6898d');
    sdk.postNftStoreFile({filePath: filePath},
        {accept: 'application/json'},
                            )
      .then(({ data }) => console.log(data))
      .catch(err => console.error(err));

def download_file(link):
    window.open(link, '_blank').focus();
