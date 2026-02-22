"""SwSystemconstDependentFormula AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1006)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 79)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 240)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.MSR.DataDictionary.SystemConstant.sw_systemconst import (
    SwSystemconst,
)
from abc import ABC, abstractmethod


class SwSystemconstDependentFormula(ARObject, ABC):
    """AUTOSAR SwSystemconstDependentFormula."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    sysc_ref: Optional[ARRef]
    sysc_string_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SwSystemconstDependentFormula."""
        super().__init__()
        self.sysc_ref: Optional[ARRef] = None
        self.sysc_string_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SwSystemconstDependentFormula to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwSystemconstDependentFormula, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sysc_ref
        if self.sysc_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sysc_ref, "SwSystemconst")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYSC-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sysc_string_ref
        if self.sysc_string_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sysc_string_ref, "SwSystemconst")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYSC-STRING-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwSystemconstDependentFormula":
        """Deserialize XML element to SwSystemconstDependentFormula object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwSystemconstDependentFormula object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwSystemconstDependentFormula, cls).deserialize(element)

        # Parse sysc_ref
        child = SerializationHelper.find_child_element(element, "SYSC-REF")
        if child is not None:
            sysc_ref_value = ARRef.deserialize(child)
            obj.sysc_ref = sysc_ref_value

        # Parse sysc_string_ref
        child = SerializationHelper.find_child_element(element, "SYSC-STRING-REF")
        if child is not None:
            sysc_string_ref_value = ARRef.deserialize(child)
            obj.sysc_string_ref = sysc_string_ref_value

        return obj



