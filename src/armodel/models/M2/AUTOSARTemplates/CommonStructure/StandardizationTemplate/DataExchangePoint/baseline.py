"""Baseline AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 79)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1.documentation import (
    Documentation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_def import (
    SdgDef,
)


class Baseline(ARObject):
    """AUTOSAR Baseline."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    custom_sdg_defs: list[SdgDef]
    customs: list[Documentation]
    standards: list[String]
    def __init__(self) -> None:
        """Initialize Baseline."""
        super().__init__()
        self.custom_sdg_defs: list[SdgDef] = []
        self.customs: list[Documentation] = []
        self.standards: list[String] = []
    def serialize(self) -> ET.Element:
        """Serialize Baseline to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize custom_sdg_defs (list to container "CUSTOM-SDG-DEFS")
        if self.custom_sdg_defs:
            wrapper = ET.Element("CUSTOM-SDG-DEFS")
            for item in self.custom_sdg_defs:
                serialized = ARObject._serialize_item(item, "SdgDef")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize customs (list to container "CUSTOMS")
        if self.customs:
            wrapper = ET.Element("CUSTOMS")
            for item in self.customs:
                serialized = ARObject._serialize_item(item, "Documentation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize standards (list to container "STANDARDS")
        if self.standards:
            wrapper = ET.Element("STANDARDS")
            for item in self.standards:
                serialized = ARObject._serialize_item(item, "String")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Baseline":
        """Deserialize XML element to Baseline object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Baseline object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse custom_sdg_defs (list from container "CUSTOM-SDG-DEFS")
        obj.custom_sdg_defs = []
        container = ARObject._find_child_element(element, "CUSTOM-SDG-DEFS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.custom_sdg_defs.append(child_value)

        # Parse customs (list from container "CUSTOMS")
        obj.customs = []
        container = ARObject._find_child_element(element, "CUSTOMS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.customs.append(child_value)

        # Parse standards (list from container "STANDARDS")
        obj.standards = []
        container = ARObject._find_child_element(element, "STANDARDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.standards.append(child_value)

        return obj



class BaselineBuilder:
    """Builder for Baseline."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Baseline = Baseline()

    def build(self) -> Baseline:
        """Build and return Baseline object.

        Returns:
            Baseline instance
        """
        # TODO: Add validation
        return self._obj
