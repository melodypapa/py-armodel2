"""CompuConstTextContent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 388)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2010)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_const_content import (
    CompuConstContent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    VerbatimString,
)
from armodel.serialization.name_converter import NameConverter

if TYPE_CHECKING:
    from typing import Self


class CompuConstTextContent(CompuConstContent):
    """AUTOSAR CompuConstTextContent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    vt: Optional[VerbatimString]
    def __init__(self) -> None:
        """Initialize CompuConstTextContent."""
        super().__init__()
        self.vt: Optional[VerbatimString] = None

    def serialize(self) -> ET.Element:
        """Serialize CompuConstTextContent to XML element.

        The VT element is serialized as a child element with text content.

        Returns:
            xml.etree.ElementTree.Element representing this CompuConstTextContent
        """
        # Use VT as the XML tag name (as specified in AUTOSAR schema)
        tag = "VT"
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes (checksum, timestamp)
        parent_elem = super(CompuConstTextContent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Serialize vt value as text content
        if self.vt is not None:
            elem.text = str(self.vt.value) if hasattr(self.vt, 'value') else str(self.vt)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> Self:
        """Deserialize XML element to CompuConstTextContent.

        The VT element's text content is deserialized to the vt attribute.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CompuConstTextContent instance
        """
        # First, call parent's deserialize to handle inherited attributes (checksum, timestamp)
        obj = super(CompuConstTextContent, cls).deserialize(element)

        # Deserialize text content to vt attribute
        if element.text:
            obj.vt = VerbatimString(value=element.text)

        return obj


class CompuConstTextContentBuilder:
    """Builder for CompuConstTextContent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuConstTextContent = CompuConstTextContent()

    def build(self) -> CompuConstTextContent:
        """Build and return CompuConstTextContent object.

        Returns:
            CompuConstTextContent instance
        """
        # TODO: Add validation
        return self._obj
