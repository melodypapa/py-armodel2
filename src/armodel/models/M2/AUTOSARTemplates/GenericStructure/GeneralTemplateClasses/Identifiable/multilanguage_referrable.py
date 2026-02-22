"""MultilanguageReferrable AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 179)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 301)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1000)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 48)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 75)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 63)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 197)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_Identifiable.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
    MultilanguageLongName,
)
from abc import ABC, abstractmethod


class MultilanguageReferrable(Referrable, ABC):
    """AUTOSAR MultilanguageReferrable."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    long_name: Optional[MultilanguageLongName]
    def __init__(self) -> None:
        """Initialize MultilanguageReferrable."""
        super().__init__()
        self.long_name: Optional[MultilanguageLongName] = None

    def serialize(self) -> ET.Element:
        """Serialize MultilanguageReferrable to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MultilanguageReferrable, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize long_name
        if self.long_name is not None:
            serialized = SerializationHelper.serialize_item(self.long_name, "MultilanguageLongName")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LONG-NAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultilanguageReferrable":
        """Deserialize XML element to MultilanguageReferrable object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MultilanguageReferrable object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MultilanguageReferrable, cls).deserialize(element)

        # Parse long_name
        child = SerializationHelper.find_child_element(element, "LONG-NAME")
        if child is not None:
            long_name_value = SerializationHelper.deserialize_with_type(child, "MultilanguageLongName")
            obj.long_name = long_name_value

        return obj



