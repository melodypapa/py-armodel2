"""PrivacyLevel AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 18)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_LogAndTraceExtract.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_method import (
    CompuMethod,
)


class PrivacyLevel(ARObject):
    """AUTOSAR PrivacyLevel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    compu_method_ref: Optional[ARRef]
    privacy_level: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize PrivacyLevel."""
        super().__init__()
        self.compu_method_ref: Optional[ARRef] = None
        self.privacy_level: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize PrivacyLevel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PrivacyLevel, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize compu_method_ref
        if self.compu_method_ref is not None:
            serialized = SerializationHelper.serialize_item(self.compu_method_ref, "CompuMethod")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMPU-METHOD-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize privacy_level
        if self.privacy_level is not None:
            serialized = SerializationHelper.serialize_item(self.privacy_level, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRIVACY-LEVEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PrivacyLevel":
        """Deserialize XML element to PrivacyLevel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PrivacyLevel object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PrivacyLevel, cls).deserialize(element)

        # Parse compu_method_ref
        child = SerializationHelper.find_child_element(element, "COMPU-METHOD-REF")
        if child is not None:
            compu_method_ref_value = ARRef.deserialize(child)
            obj.compu_method_ref = compu_method_ref_value

        # Parse privacy_level
        child = SerializationHelper.find_child_element(element, "PRIVACY-LEVEL")
        if child is not None:
            privacy_level_value = child.text
            obj.privacy_level = privacy_level_value

        return obj



class PrivacyLevelBuilder:
    """Builder for PrivacyLevel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PrivacyLevel = PrivacyLevel()

    def build(self) -> PrivacyLevel:
        """Build and return PrivacyLevel object.

        Returns:
            PrivacyLevel instance
        """
        # TODO: Add validation
        return self._obj
