"""BswExclusiveAreaPolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 82)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import (
    ApiPrincipleEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area import (
    ExclusiveArea,
)


class BswExclusiveAreaPolicy(ARObject):
    """AUTOSAR BswExclusiveAreaPolicy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    api_principle_enum: Optional[ApiPrincipleEnum]
    exclusive_area_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize BswExclusiveAreaPolicy."""
        super().__init__()
        self.api_principle_enum: Optional[ApiPrincipleEnum] = None
        self.exclusive_area_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize BswExclusiveAreaPolicy to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize api_principle_enum
        if self.api_principle_enum is not None:
            serialized = ARObject._serialize_item(self.api_principle_enum, "ApiPrincipleEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("API-PRINCIPLE-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize exclusive_area_ref
        if self.exclusive_area_ref is not None:
            serialized = ARObject._serialize_item(self.exclusive_area_ref, "ExclusiveArea")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXCLUSIVE-AREA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswExclusiveAreaPolicy":
        """Deserialize XML element to BswExclusiveAreaPolicy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswExclusiveAreaPolicy object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse api_principle_enum
        child = ARObject._find_child_element(element, "API-PRINCIPLE-ENUM")
        if child is not None:
            api_principle_enum_value = ApiPrincipleEnum.deserialize(child)
            obj.api_principle_enum = api_principle_enum_value

        # Parse exclusive_area_ref
        child = ARObject._find_child_element(element, "EXCLUSIVE-AREA-REF")
        if child is not None:
            exclusive_area_ref_value = ARRef.deserialize(child)
            obj.exclusive_area_ref = exclusive_area_ref_value

        return obj



class BswExclusiveAreaPolicyBuilder:
    """Builder for BswExclusiveAreaPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswExclusiveAreaPolicy = BswExclusiveAreaPolicy()

    def build(self) -> BswExclusiveAreaPolicy:
        """Build and return BswExclusiveAreaPolicy object.

        Returns:
            BswExclusiveAreaPolicy instance
        """
        # TODO: Add validation
        return self._obj
