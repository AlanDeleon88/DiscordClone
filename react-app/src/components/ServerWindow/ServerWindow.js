import './ServerWindow.css'
import { Switch, useParams,Route, useRouteMatch, NavLink } from 'react-router-dom'
import ChannelList from './ChannelList/ChannelList';
import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getIdServer } from '../../store/focusServer';
import MessageWindow from './MessageWindow';
import ServerOptions from './ServerOptions';
import {IoSettingsSharp} from 'react-icons/io5'
import UserBox from '../UserBoxComponent';
import User from '../User';
const ServerWindow = () =>{
    const [isLoaded, setIsLoaded] = useState(false);
    const [myServer, setMyServer] = useState(false);
    let {serverId} = useParams();
    let id = Number(serverId);
    const server = useSelector(state => state.focusServer)
    const user = useSelector(state=>state.session.user)
    const dispatch = useDispatch();
    const match = useRouteMatch();

    useEffect(() =>{
        dispatch(getIdServer(id)).then(() =>{
            setIsLoaded(true)
            // console.log('IM THE ONE');
        })
    },[dispatch])

    //!use props to thread through message window maybe.
    return (
        <>
            <div className='main-view'>

                <Switch>
                    <Route path={match.url} exact={true}>
                        TESTING
                    </Route>
                    <Route path={`${match.url}/channel`}>
                    <div className='channel-container'>
                        {isLoaded &&
                            (
                            <>

                                <div className='server-title'>

                                        <ServerOptions userId={user.id} serverId={server.id} server={server}/>

                                </div>

                                <div className='channel-list-user-box'>
                                    <ChannelList id = {id}/>

                                    {/* make this userbox into a component..*/}
                                    <UserBox />

                                </div>


                            </>

                            )
                        }
                    </div>

                        <MessageWindow />
                    </Route>
                </Switch>
            </div>



        </>
    )

}

export default ServerWindow
