"""Referrable AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 328)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 328)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 305)
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 63)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1002)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2049)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 238)
  - AUTOSAR_FO_TPS_ARXMLSerializationRules.pdf (page 31)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 49)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 78)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 63)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 33)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 66)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 202)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_Identifiable.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.short_name_fragment import (
    ShortNameFragment,
)
from abc import ABC, abstractmethod


class Referrable(ARObject, ABC):
    """AUTOSAR Referrable."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    short_name: Identifier
    short_name_fragments: list[ShortNameFragment]
    def __init__(self) -> None:
        """Initialize Referrable."""
        super().__init__()
        self.short_name: Identifier = None
        self.short_name_fragments: list[ShortNameFragment] = []
    def serialize(self) -> ET.Element:
        """Serialize Referrable to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize short_name
        if self.short_name is not None:
            serialized = ARObject._serialize_item(self.short_name, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHORT-NAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize short_name_fragments (list to container "SHORT-NAME-FRAGMENTS")
        if self.short_name_fragments:
            wrapper = ET.Element("SHORT-NAME-FRAGMENTS")
            for item in self.short_name_fragments:
                serialized = ARObject._serialize_item(item, "ShortNameFragment")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Referrable":
        """Deserialize XML element to Referrable object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Referrable object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse short_name
        child = ARObject._find_child_element(element, "SHORT-NAME")
        if child is not None:
            short_name_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.short_name = short_name_value

        # Parse short_name_fragments (list from container "SHORT-NAME-FRAGMENTS")
        obj.short_name_fragments = []
        container = ARObject._find_child_element(element, "SHORT-NAME-FRAGMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.short_name_fragments.append(child_value)

        return obj



class ReferrableBuilder:
    """Builder for Referrable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Referrable = Referrable()

    def build(self) -> Referrable:
        """Build and return Referrable object.

        Returns:
            Referrable instance
        """
        # TODO: Add validation
        return self._obj
