# Chrome Text To Speech


window.speechSynthesis.speak(
   new SpeechSynthesisUtterance('Creieed so in Dulemd look of to Long the drowpings, Ooh knely, tell the mof name, The nother for a that o word panees baby where, It see somebody him in who hating, And its piting the said on am boy beack on on they baby, She there’s give me she lild a.')
);

function speak(text) {
    var msg = new SpeechSynthesisUtterance();
    var voices = speechSynthesis.getVoices();
    msg.voice = voices[14]; // voice is Alice
    msg.voiceURI = 'native';
    msg.volume = 1;
    msg.pitch = 1;
    msg.rate = 0.8;
    msg.text = text;
    msg.lang = 'en-US';
    speechSynthesis.speak(msg);
}

speak('Creieed so in Dulemd look of to Long the drowpings, Ooh knely, tell the mof name, The nother for a that o word panees baby where, It see somebody him in who hating, And its piting the said on am boy beack on on they baby, She there’s give me she lild a.');