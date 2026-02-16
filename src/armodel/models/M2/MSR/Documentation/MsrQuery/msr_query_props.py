"""MsrQueryProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_arg import (
    MsrQueryArg,
)


class MsrQueryProps(ARObject):
    """AUTOSAR MsrQueryProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("comment", None, True, False, None),  # comment
        ("msr_query_args", None, False, True, MsrQueryArg),  # msrQueryArgs
        ("msr_query_name", None, True, False, None),  # msrQueryName
    ]

    def __init__(self) -> None:
        """Initialize MsrQueryProps."""
        super().__init__()
        self.comment: Optional[String] = None
        self.msr_query_args: list[MsrQueryArg] = []
        self.msr_query_name: String = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MsrQueryProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MsrQueryProps":
        """Create MsrQueryProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MsrQueryProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MsrQueryProps since parent returns ARObject
        return cast("MsrQueryProps", obj)


class MsrQueryPropsBuilder:
    """Builder for MsrQueryProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MsrQueryProps = MsrQueryProps()

    def build(self) -> MsrQueryProps:
        """Build and return MsrQueryProps object.

        Returns:
            MsrQueryProps instance
        """
        # TODO: Add validation
        return self._obj
