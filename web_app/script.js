const apiUrl = 'http://127.0.0.1:8000/urlapp/check/';

const checkUrl = async (url) => {
  try {
    const response = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ url }),
    });

    const result = await response.json();
    
    // Process the result and update your frontend UI
    console.log('Is malicious:', result.is_malicious);
  } catch (error) {
    console.log('Error:', error);
  }
};



// Call the function with a URL to check
checkUrl('webdav1.storegate.com/uwiq175/home/uwiq175');