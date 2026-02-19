"""BswModuleDependency AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 47)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswInterfaces.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview.bsw_module_description import (
        BswModuleDescription,
    )



class BswModuleDependency(Identifiable):
    """AUTOSAR BswModuleDependency."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    target_module_id: Optional[PositiveInteger]
    target_module: Optional[BswModuleDescription]
    def __init__(self) -> None:
        """Initialize BswModuleDependency."""
        super().__init__()
        self.target_module_id: Optional[PositiveInteger] = None
        self.target_module: Optional[BswModuleDescription] = None
    def serialize(self) -> ET.Element:
        """Serialize BswModuleDependency to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswModuleDependency, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize target_module_id
        if self.target_module_id is not None:
            serialized = ARObject._serialize_item(self.target_module_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-MODULE-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_module
        if self.target_module is not None:
            serialized = ARObject._serialize_item(self.target_module, "BswModuleDescription")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-MODULE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModuleDependency":
        """Deserialize XML element to BswModuleDependency object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswModuleDependency object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswModuleDependency, cls).deserialize(element)

        # Parse target_module_id
        child = ARObject._find_child_element(element, "TARGET-MODULE-ID")
        if child is not None:
            target_module_id_value = child.text
            obj.target_module_id = target_module_id_value

        # Parse target_module
        child = ARObject._find_child_element(element, "TARGET-MODULE")
        if child is not None:
            target_module_value = ARObject._deserialize_by_tag(child, "BswModuleDescription")
            obj.target_module = target_module_value

        return obj



class BswModuleDependencyBuilder:
    """Builder for BswModuleDependency."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModuleDependency = BswModuleDependency()

    def build(self) -> BswModuleDependency:
        """Build and return BswModuleDependency object.

        Returns:
            BswModuleDependency instance
        """
        # TODO: Add validation
        return self._obj
