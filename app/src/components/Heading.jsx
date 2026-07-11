const Heading = ({ children, size, className }) => {
    const headingClasses = `title is-size-${size} ${className}`.trim()
    
    return (
        <h1 className={headingClasses}>
            {children}
        </h1>
    )
}

export default Heading