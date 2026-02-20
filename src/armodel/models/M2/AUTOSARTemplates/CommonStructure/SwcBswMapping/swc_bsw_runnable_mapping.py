"""SwcBswRunnableMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 110)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_SwcBswMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import (
    BswModuleEntity,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.runnable_entity import (
    RunnableEntity,
)


class SwcBswRunnableMapping(ARObject):
    """AUTOSAR SwcBswRunnableMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bsw_entity: Optional[BswModuleEntity]
    swc_runnable: Optional[RunnableEntity]
    def __init__(self) -> None:
        """Initialize SwcBswRunnableMapping."""
        super().__init__()
        self.bsw_entity: Optional[BswModuleEntity] = None
        self.swc_runnable: Optional[RunnableEntity] = None

    def serialize(self) -> ET.Element:
        """Serialize SwcBswRunnableMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize bsw_entity
        if self.bsw_entity is not None:
            serialized = ARObject._serialize_item(self.bsw_entity, "BswModuleEntity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BSW-ENTITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize swc_runnable
        if self.swc_runnable is not None:
            serialized = ARObject._serialize_item(self.swc_runnable, "RunnableEntity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SWC-RUNNABLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcBswRunnableMapping":
        """Deserialize XML element to SwcBswRunnableMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcBswRunnableMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse bsw_entity
        child = ARObject._find_child_element(element, "BSW-ENTITY")
        if child is not None:
            bsw_entity_value = ARObject._deserialize_by_tag(child, "BswModuleEntity")
            obj.bsw_entity = bsw_entity_value

        # Parse swc_runnable
        child = ARObject._find_child_element(element, "SWC-RUNNABLE")
        if child is not None:
            swc_runnable_value = ARObject._deserialize_by_tag(child, "RunnableEntity")
            obj.swc_runnable = swc_runnable_value

        return obj



class SwcBswRunnableMappingBuilder:
    """Builder for SwcBswRunnableMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcBswRunnableMapping = SwcBswRunnableMapping()

    def build(self) -> SwcBswRunnableMapping:
        """Build and return SwcBswRunnableMapping object.

        Returns:
            SwcBswRunnableMapping instance
        """
        # TODO: Add validation
        return self._obj
