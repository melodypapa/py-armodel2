"""AccessCount AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 57)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_AccessCount.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)


class AccessCount(ARObject):
    """AUTOSAR AccessCount."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    access_point_ref: Optional[ARRef]
    value: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize AccessCount."""
        super().__init__()
        self.access_point_ref: Optional[ARRef] = None
        self.value: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize AccessCount to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize access_point_ref
        if self.access_point_ref is not None:
            serialized = ARObject._serialize_item(self.access_point_ref, "AbstractAccessPoint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACCESS-POINT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize value
        if self.value is not None:
            serialized = ARObject._serialize_item(self.value, "PositiveInteger")
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
    def deserialize(cls, element: ET.Element) -> "AccessCount":
        """Deserialize XML element to AccessCount object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AccessCount object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse access_point_ref
        child = ARObject._find_child_element(element, "ACCESS-POINT-REF")
        if child is not None:
            access_point_ref_value = ARRef.deserialize(child)
            obj.access_point_ref = access_point_ref_value

        # Parse value
        child = ARObject._find_child_element(element, "VALUE")
        if child is not None:
            value_value = child.text
            obj.value = value_value

        return obj



class AccessCountBuilder:
    """Builder for AccessCount."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AccessCount = AccessCount()

    def build(self) -> AccessCount:
        """Build and return AccessCount object.

        Returns:
            AccessCount instance
        """
        # TODO: Add validation
        return self._obj
