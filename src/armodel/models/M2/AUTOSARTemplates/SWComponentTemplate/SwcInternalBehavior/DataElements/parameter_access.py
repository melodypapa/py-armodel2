"""ParameterAccess AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_parameter_ref import (
    AutosarParameterRef,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)


class ParameterAccess(AbstractAccessPoint):
    """AUTOSAR ParameterAccess."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("accessed_parameter", None, False, False, AutosarParameterRef),  # accessedParameter
        ("sw_data_def", None, False, False, SwDataDefProps),  # swDataDef
    ]

    def __init__(self) -> None:
        """Initialize ParameterAccess."""
        super().__init__()
        self.accessed_parameter: Optional[AutosarParameterRef] = None
        self.sw_data_def: Optional[SwDataDefProps] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ParameterAccess to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ParameterAccess":
        """Create ParameterAccess from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ParameterAccess instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ParameterAccess since parent returns ARObject
        return cast("ParameterAccess", obj)


class ParameterAccessBuilder:
    """Builder for ParameterAccess."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ParameterAccess = ParameterAccess()

    def build(self) -> ParameterAccess:
        """Build and return ParameterAccess object.

        Returns:
            ParameterAccess instance
        """
        # TODO: Add validation
        return self._obj
