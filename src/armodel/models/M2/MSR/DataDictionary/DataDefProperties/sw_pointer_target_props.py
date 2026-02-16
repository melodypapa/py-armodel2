"""SwPointerTargetProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)


class SwPointerTargetProps(ARObject):
    """AUTOSAR SwPointerTargetProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("function_pointer", None, False, False, BswModuleEntry),  # functionPointer
        ("sw_data_def", None, False, False, SwDataDefProps),  # swDataDef
        ("target_category", None, True, False, None),  # targetCategory
    ]

    def __init__(self) -> None:
        """Initialize SwPointerTargetProps."""
        super().__init__()
        self.function_pointer: Optional[BswModuleEntry] = None
        self.sw_data_def: Optional[SwDataDefProps] = None
        self.target_category: Optional[Identifier] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwPointerTargetProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwPointerTargetProps":
        """Create SwPointerTargetProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwPointerTargetProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwPointerTargetProps since parent returns ARObject
        return cast("SwPointerTargetProps", obj)


class SwPointerTargetPropsBuilder:
    """Builder for SwPointerTargetProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwPointerTargetProps = SwPointerTargetProps()

    def build(self) -> SwPointerTargetProps:
        """Build and return SwPointerTargetProps object.

        Returns:
            SwPointerTargetProps instance
        """
        # TODO: Add validation
        return self._obj
