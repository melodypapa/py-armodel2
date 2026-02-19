"""BinaryManifestItemNumericalValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 922)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster_BinaryManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_item_value import (
    BinaryManifestItemValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)


class BinaryManifestItemNumericalValue(BinaryManifestItemValue):
    """AUTOSAR BinaryManifestItemNumericalValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    value: Optional[Numerical]
    def __init__(self) -> None:
        """Initialize BinaryManifestItemNumericalValue."""
        super().__init__()
        self.value: Optional[Numerical] = None
    def serialize(self) -> ET.Element:
        """Serialize BinaryManifestItemNumericalValue to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BinaryManifestItemNumericalValue, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize value
        if self.value is not None:
            serialized = ARObject._serialize_item(self.value, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BinaryManifestItemNumericalValue":
        """Deserialize XML element to BinaryManifestItemNumericalValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BinaryManifestItemNumericalValue object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BinaryManifestItemNumericalValue, cls).deserialize(element)

        # Parse value
        child = ARObject._find_child_element(element, "VALUE")
        if child is not None:
            value_value = child.text
            obj.value = value_value

        return obj



class BinaryManifestItemNumericalValueBuilder:
    """Builder for BinaryManifestItemNumericalValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestItemNumericalValue = BinaryManifestItemNumericalValue()

    def build(self) -> BinaryManifestItemNumericalValue:
        """Build and return BinaryManifestItemNumericalValue object.

        Returns:
            BinaryManifestItemNumericalValue instance
        """
        # TODO: Add validation
        return self._obj
