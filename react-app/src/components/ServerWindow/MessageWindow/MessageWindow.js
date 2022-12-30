import './MessageWindow.css'
import { useParams } from 'react-router-dom';
import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getChannel } from '../../../store/channel';
import { getChannelMessages } from '../../../store/channelMessage';
import ChannelHeader from '../ChannelHeader/ChannelHeader';
import MessageComponent from '../MessageComponent';


const MessageWindow = ({type, channelId}) =>{

    const [isLoaded, setIsLoaded] = useState(false)
    const dispatch = useDispatch()
    const channel = useSelector(state => state.channel)
    const messages = Object.values(useSelector(state=>state.channelMessages))




    useEffect(() =>{
        dispatch(getChannelMessages(channelId)).then(() =>{

            // console.log(isLoaded);
        })
        setIsLoaded(true)
    },[dispatch])



    return(
        <>
            <div className="message-container">
                { type === 'channel' &&
                    <>

                    <div>
                        {/*place holder div*/}
                    </div>
                    <div>
                        {isLoaded && (
                            <>
                                {/*make message component later, pass message into component..*/}
                                {messages.map(el =>{
                                    return(
                                        <MessageComponent message={el} />
                                    )
                                })}
                            </>
                        )}

                    </div>

                    </>
                }
                { type === 'dm' &&

                    <>
                        <div>
                        {/*place holder div*/}
                        </div>

                        <div>
                            DM messages will go here.
                        </div>

                    </>

                }
            </div>

        </>
    )

}

export default MessageWindow
