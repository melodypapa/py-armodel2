"""IdsDesign AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 16)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_common_element import (
    IdsCommonElement,
)


class IdsDesign(ARElement):
    """AUTOSAR IdsDesign."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    element_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize IdsDesign."""
        super().__init__()
        self.element_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize IdsDesign to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IdsDesign, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize element_refs (list to container "ELEMENT-REFS")
        if self.element_refs:
            wrapper = ET.Element("ELEMENT-REFS")
            for item in self.element_refs:
                serialized = ARObject._serialize_item(item, "IdsCommonElement")
                if serialized is not None:
                    child_elem = ET.Element("ELEMENT-REF")
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
    def deserialize(cls, element: ET.Element) -> "IdsDesign":
        """Deserialize XML element to IdsDesign object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IdsDesign object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IdsDesign, cls).deserialize(element)

        # Parse element_refs (list from container "ELEMENT-REFS")
        obj.element_refs = []
        container = ARObject._find_child_element(element, "ELEMENT-REFS")
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
                    obj.element_refs.append(child_value)

        return obj



class IdsDesignBuilder:
    """Builder for IdsDesign."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsDesign = IdsDesign()

    def build(self) -> IdsDesign:
        """Build and return IdsDesign object.

        Returns:
            IdsDesign instance
        """
        # TODO: Add validation
        return self._obj
