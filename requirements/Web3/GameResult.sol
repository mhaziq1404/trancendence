// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract GameResults {
    struct Result {
        string player;
        uint256 score;
    }

    Result[] public results;

    function storeResult(string memory player, uint256 score) public {
        results.push(Result(player, score));
    }

    function getResult(uint256 index) public view returns (string memory player, uint256 score) {
        Result memory result = results[index];
        return (result.player, result.score);
    }
}

