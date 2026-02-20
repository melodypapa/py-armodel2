"""ExclusiveAreaNestingOrder AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 84)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 554)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_InternalBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area import (
    ExclusiveArea,
)


class ExclusiveAreaNestingOrder(Referrable):
    """AUTOSAR ExclusiveAreaNestingOrder."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    exclusive_area_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize ExclusiveAreaNestingOrder."""
        super().__init__()
        self.exclusive_area_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize ExclusiveAreaNestingOrder to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ExclusiveAreaNestingOrder, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize exclusive_area_refs (list to container "EXCLUSIVE-AREA-REFS")
        if self.exclusive_area_refs:
            wrapper = ET.Element("EXCLUSIVE-AREA-REFS")
            for item in self.exclusive_area_refs:
                serialized = ARObject._serialize_item(item, "ExclusiveArea")
                if serialized is not None:
                    child_elem = ET.Element("EXCLUSIVE-AREA-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ExclusiveAreaNestingOrder":
        """Deserialize XML element to ExclusiveAreaNestingOrder object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ExclusiveAreaNestingOrder object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ExclusiveAreaNestingOrder, cls).deserialize(element)

        # Parse exclusive_area_refs (list from container "EXCLUSIVE-AREA-REFS")
        obj.exclusive_area_refs = []
        container = ARObject._find_child_element(element, "EXCLUSIVE-AREA-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.exclusive_area_refs.append(child_value)

        return obj



class ExclusiveAreaNestingOrderBuilder:
    """Builder for ExclusiveAreaNestingOrder."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ExclusiveAreaNestingOrder = ExclusiveAreaNestingOrder()

    def build(self) -> ExclusiveAreaNestingOrder:
        """Build and return ExclusiveAreaNestingOrder object.

        Returns:
            ExclusiveAreaNestingOrder instance
        """
        # TODO: Add validation
        return self._obj
