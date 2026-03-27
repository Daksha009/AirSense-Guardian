import React, { useState, useRef, useEffect } from 'react';

const Chatbot = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [city, setCity] = useState('Delhi');
  const [message, setMessage] = useState('');
  const [messages, setMessages] = useState([
    { role: 'assistant', content: 'Hi! I am your AI Health Assistant. Ask me about the air quality and health precautions for your city.' }
  ]);
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSend = async (e) => {
    e.preventDefault();
    if (!message.trim() || !city.trim()) return;

    const userMsg = message;
    setMessage('');
    setMessages(prev => [...prev, { role: 'user', content: userMsg }]);
    setIsLoading(true);

    try {
      const response = await fetch('http://localhost:5000/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ city, message: userMsg })
      });

      const data = await response.json();
      
      if (data.error) {
        setMessages(prev => [...prev, { role: 'assistant', content: `Error: ${data.error}` }]);
      } else {
        setMessages(prev => [...prev, { role: data.role || 'assistant', content: data.content }]);
      }
    } catch (error) {
      setMessages(prev => [...prev, { role: 'assistant', content: 'Failed to connect to the assistant.' }]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="fixed bottom-6 right-6 z-50">
      {/* Chat Window */}
      {isOpen && (
        <div className="bg-[#0e110f] border border-brand-green/30 w-80 md:w-96 rounded-2xl shadow-[0_0_30px_rgba(73,167,96,0.15)] flex flex-col overflow-hidden mb-4 transition-all" style={{ height: '500px' }}>
          
          {/* Header */}
          <div className="bg-brand-green/10 border-b border-brand-green/30 p-4 flex justify-between items-center backdrop-blur-md">
            <div className="flex items-center gap-2">
              <div className="w-8 h-8 rounded-full bg-brand-green/20 flex items-center justify-center">
                <i className="fas fa-robot text-brand-green"></i>
              </div>
              <h3 className="text-white font-bold font-display">AI Assistant</h3>
            </div>
            <button onClick={() => setIsOpen(false)} className="text-gray-400 hover:text-white transition-colors">
              <i className="fas fa-times"></i>
            </button>
          </div>

          {/* City Input */}
          <div className="p-3 border-b border-white/5 bg-black/20">
            <div className="flex items-center gap-2 bg-white/5 rounded-lg px-3 py-1.5 focus-within:ring-1 ring-brand-green/50">
              <i className="fas fa-city text-gray-500 text-sm"></i>
              <input 
                type="text" 
                value={city} 
                onChange={(e) => setCity(e.target.value)}
                placeholder="City Name"
                className="bg-transparent border-none text-white text-sm w-full outline-none placeholder-gray-600"
              />
            </div>
          </div>

          {/* Messages Area */}
          <div className="flex-1 overflow-y-auto p-4 space-y-4">
            {messages.map((msg, idx) => (
              <div key={idx} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                <div className={`w-fit max-w-[85%] rounded-2xl p-3 text-sm ${
                  msg.role === 'user' 
                    ? 'bg-brand-green text-white rounded-br-none' 
                    : 'bg-white/10 text-gray-200 rounded-bl-none border border-white/5'
                }`} style={{ whiteSpace: 'pre-wrap' }}>
                  {msg.role === 'assistant' && (
                    <div className="text-[10px] text-brand-accent mb-1 uppercase tracking-wider font-bold">
                      <i className="fas fa-sparkles mr-1"></i> AI-Generated 
                    </div>
                  )}
                  {msg.content}
                </div>
              </div>
            ))}
            {isLoading && (
              <div className="flex justify-start">
                <div className="bg-white/10 rounded-2xl rounded-bl-none p-4 border border-white/5 flex gap-1 items-center">
                  <div className="w-2 h-2 rounded-full bg-brand-green animate-bounce"></div>
                  <div className="w-2 h-2 rounded-full bg-brand-green animate-bounce delay-100"></div>
                  <div className="w-2 h-2 rounded-full bg-brand-green animate-bounce delay-200"></div>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          {/* Input Area */}
          <div className="p-3 bg-black/40 border-t border-white/5 backdrop-blur-md">
            <form onSubmit={handleSend} className="flex gap-2">
              <input 
                type="text" 
                value={message} 
                onChange={(e) => setMessage(e.target.value)}
                placeholder="Ask about health risks..."
                className="flex-1 bg-white/5 border border-white/10 rounded-xl px-4 py-2 text-sm text-white focus:outline-none focus:border-brand-green/50 placeholder-gray-500"
              />
              <button 
                type="submit" 
                disabled={isLoading || !message.trim()} 
                className="bg-brand-green hover:bg-[#3d8b50] disabled:opacity-50 disabled:cursor-not-allowed text-white w-10 h-10 rounded-xl flex items-center justify-center transition-colors"
              >
                <i className="fas fa-paper-plane text-sm"></i>
              </button>
            </form>
          </div>
        </div>
      )}

      {/* Floating Button */}
      {!isOpen && (
        <button 
          onClick={() => setIsOpen(true)}
          className="bg-brand-green hover:bg-[#3d8b50] text-white w-14 h-14 rounded-full shadow-[0_0_20px_rgba(73,167,96,0.5)] flex items-center justify-center transition-transform hover:scale-110"
        >
          <i className="fas fa-comment-medical text-xl"></i>
        </button>
      )}
    </div>
  );
};

export default Chatbot;
