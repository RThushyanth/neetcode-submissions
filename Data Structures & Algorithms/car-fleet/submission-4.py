class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        dict_info = {}

        for i in range(0,len(position)):
            dict_info[position[i]] = speed[i]
        
        position.sort()

        stack = []


        def postomeet(cur_pos1,cur_pos2,spd1,spd2):
            return (((abs(cur_pos1-cur_pos2)/abs(spd1-spd2))*spd1)+cur_pos1)

        dict_fleets = {}
        k = 0
        fleets_del = 0
        for i in range(0,len(position)):
            if i == len(position) - 1:
                if dict_info[position[i]] >= dict_info[position[i-1]]:
                    try:
                        dict_fleets[k]
                    except KeyError:
                        dict_fleets[k] = [i]
                    else:
                        dict_fleets[k].append(i)
                    k = k+1
                else:
                    if postomeet(position[i],position[i-1],dict_info[position[i]],dict_info[position[i-1]]) > target:
                        try:
                            dict_fleets[k]
                        except KeyError:
                            dict_fleets[k] = [i]
                        else:
                            dict_fleets[k].append(i)
                        k = k+1
                    else:
                        try:
                            dict_fleets[k]
                        except KeyError:
                            dict_fleets[k] = [i]
                        else:
                            dict_fleets[k].append(i)

            if i != len(position) -1:
                if dict_info[position[i+1]] >= dict_info[position[i]]:
                    try:
                        dict_fleets[k]
                    except KeyError:
                        dict_fleets[k] = [i]
                    else:
                        dict_fleets[k].append(i)
                    stack.append(dict_fleets[k])
                    k = k+1

                else:
                    if postomeet(position[i],position[i+1],dict_info[position[i]],dict_info[position[i+1]]) > target:
                        try:
                            dict_fleets[k]
                        except KeyError:
                            dict_fleets[k] = [i]
                        else:
                            dict_fleets[k].append(i)
                        stack.append(dict_fleets[k])
                        k = k+1
                    else:
                        try:
                            dict_fleets[k]
                        except KeyError:
                            dict_fleets[k] = [i]
                        else:
                            dict_fleets[k].append(i)
                        if len(stack) != 0: 
                            while len(stack) != 0 and dict_info[position[stack[-1][-1]]] > dict_info[position[i+1]] and postomeet(position[stack[-1][-1]],position[i+1],dict_info[position[stack[-1][-1]]],dict_info[position[i+1]]) <= target:
                                dict_fleets[k].extend(stack[-1])
                                fleets_del = fleets_del + 1
                                stack.pop()                            
        
        return len(dict_fleets) - fleets_del


                