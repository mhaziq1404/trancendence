// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract GameResults {
    struct Game {
        address player;
        uint score;
        uint timestamp;
    }

    Game[] public games;

    event GameResultStored(address indexed player, uint score, uint indexed timestamp);

    function storeGameResult(uint _score) public {
        Game memory newGame = Game(msg.sender, _score, block.timestamp);
        games.push(newGame);
        emit GameResultStored(msg.sender, _score, block.timestamp);
    }

    function getGameCount() public view returns (uint) {
        return games.length;
    }

    function getGame(uint _index) public view returns (address player, uint score, uint timestamp) {
        Game storage game = games[_index];
        return (game.player, game.score, game.timestamp);
    }
}
