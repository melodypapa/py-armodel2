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

    sysc: Optional[SwSystemconst]
    sysc_string: Optional[SwSystemconst]
    def __init__(self) -> None:
        """Initialize SwSystemconstDependentFormula."""
        super().__init__()
        self.sysc: Optional[SwSystemconst] = None
        self.sysc_string: Optional[SwSystemconst] = None

    def serialize(self) -> ET.Element:
        """Serialize SwSystemconstDependentFormula to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize sysc
        if self.sysc is not None:
            serialized = ARObject._serialize_item(self.sysc, "SwSystemconst")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYSC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sysc_string
        if self.sysc_string is not None:
            serialized = ARObject._serialize_item(self.sysc_string, "SwSystemconst")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYSC-STRING")
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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse sysc
        child = ARObject._find_child_element(element, "SYSC")
        if child is not None:
            sysc_value = ARObject._deserialize_by_tag(child, "SwSystemconst")
            obj.sysc = sysc_value

        # Parse sysc_string
        child = ARObject._find_child_element(element, "SYSC-STRING")
        if child is not None:
            sysc_string_value = ARObject._deserialize_by_tag(child, "SwSystemconst")
            obj.sysc_string = sysc_string_value

        return obj



class SwSystemconstDependentFormulaBuilder:
    """Builder for SwSystemconstDependentFormula."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwSystemconstDependentFormula = SwSystemconstDependentFormula()

    def build(self) -> SwSystemconstDependentFormula:
        """Build and return SwSystemconstDependentFormula object.

        Returns:
            SwSystemconstDependentFormula instance
        """
        # TODO: Add validation
        return self._obj
