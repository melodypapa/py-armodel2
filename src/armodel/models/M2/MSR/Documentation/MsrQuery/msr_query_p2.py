"""MsrQueryP2 AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_props import (
    MsrQueryProps,
)


class MsrQueryP2(ARObject):
    """AUTOSAR MsrQueryP2."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("msr_query_props", None, False, False, MsrQueryProps),  # msrQueryProps
        ("msr_query_result", None, False, False, DocumentationBlock),  # msrQueryResult
    ]

    def __init__(self) -> None:
        """Initialize MsrQueryP2."""
        super().__init__()
        self.msr_query_props: MsrQueryProps = None
        self.msr_query_result: Optional[DocumentationBlock] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MsrQueryP2 to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MsrQueryP2":
        """Create MsrQueryP2 from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MsrQueryP2 instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MsrQueryP2 since parent returns ARObject
        return cast("MsrQueryP2", obj)


class MsrQueryP2Builder:
    """Builder for MsrQueryP2."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MsrQueryP2 = MsrQueryP2()

    def build(self) -> MsrQueryP2:
        """Build and return MsrQueryP2 object.

        Returns:
            MsrQueryP2 instance
        """
        # TODO: Add validation
        return self._obj
