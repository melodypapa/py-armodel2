"""CryptoServiceQueue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 381)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CryptoServiceQueue(ARElement):
    """AUTOSAR CryptoServiceQueue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    queue_size: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize CryptoServiceQueue."""
        super().__init__()
        self.queue_size: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize CryptoServiceQueue to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CryptoServiceQueue, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize queue_size
        if self.queue_size is not None:
            serialized = SerializationHelper.serialize_item(self.queue_size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("QUEUE-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CryptoServiceQueue":
        """Deserialize XML element to CryptoServiceQueue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CryptoServiceQueue object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CryptoServiceQueue, cls).deserialize(element)

        # Parse queue_size
        child = SerializationHelper.find_child_element(element, "QUEUE-SIZE")
        if child is not None:
            queue_size_value = child.text
            obj.queue_size = queue_size_value

        return obj



class CryptoServiceQueueBuilder:
    """Builder for CryptoServiceQueue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CryptoServiceQueue = CryptoServiceQueue()

    def build(self) -> CryptoServiceQueue:
        """Build and return CryptoServiceQueue object.

        Returns:
            CryptoServiceQueue instance
        """
        # TODO: Add validation
        return self._obj
