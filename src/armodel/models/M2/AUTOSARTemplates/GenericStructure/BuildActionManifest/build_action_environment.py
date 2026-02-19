"""BuildActionEnvironment AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 370)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 173)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_BuildActionManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.SpecialData.sdg import (
    Sdg,
)


class BuildActionEnvironment(Identifiable):
    """AUTOSAR BuildActionEnvironment."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sdgs: list[Sdg]
    def __init__(self) -> None:
        """Initialize BuildActionEnvironment."""
        super().__init__()
        self.sdgs: list[Sdg] = []

    def serialize(self) -> ET.Element:
        """Serialize BuildActionEnvironment to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BuildActionEnvironment, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sdgs (list to container "SDGS")
        if self.sdgs:
            wrapper = ET.Element("SDGS")
            for item in self.sdgs:
                serialized = ARObject._serialize_item(item, "Sdg")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BuildActionEnvironment":
        """Deserialize XML element to BuildActionEnvironment object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BuildActionEnvironment object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BuildActionEnvironment, cls).deserialize(element)

        # Parse sdgs (list from container "SDGS")
        obj.sdgs = []
        container = ARObject._find_child_element(element, "SDGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sdgs.append(child_value)

        return obj



class BuildActionEnvironmentBuilder:
    """Builder for BuildActionEnvironment."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BuildActionEnvironment = BuildActionEnvironment()

    def build(self) -> BuildActionEnvironment:
        """Build and return BuildActionEnvironment object.

        Returns:
            BuildActionEnvironment instance
        """
        # TODO: Add validation
        return self._obj
