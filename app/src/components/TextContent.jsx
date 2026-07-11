const TextContent = ({ children, size, className }) => {
    const textClasses = `content is-size-${size} ${className}`.trim()
    
    return (
        <p className={textClasses}>
            {children}
        </p>
    )
}

export default TextContent