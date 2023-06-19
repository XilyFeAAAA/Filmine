export const verify = () => {
    const token = localStorage.getItem('token')
    if (token === null) {
        return Promise.resolve(false)
    } else {
        return fetch('http://localhost:7070/user/verify', {
            method: 'POST',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json',
                Authorization: token,
            },
        })
            .then((response) => {
                return response.json().then((data) => {
                    if (data.code == 200) {
                        return true
                    } else {
                        // 验证不通过则返回登录页
                        localStorage.removeItem('token')
                        return false
                    }
                })
            })
            .catch((error) => {
                console.error(error)
                return false
            })
    }
}
