import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { User } from './entities/user.entity';

@Injectable()
export class UserService {
    constructor(@InjectRepository(User) private userRespository: Repository<User>){}

    async findOne(email: string): Promise<User>{
        return await this.userRespository.findOne({where: {email:email}});
    }
}
