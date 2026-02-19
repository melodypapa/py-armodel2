"""CryptoServiceNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 235)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 733)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)


class CryptoServiceNeeds(ServiceNeeds):
    """AUTOSAR CryptoServiceNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    algorithm_family: Optional[String]
    algorithm_mode: Optional[String]
    crypto_key: Optional[String]
    maximum_key: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize CryptoServiceNeeds."""
        super().__init__()
        self.algorithm_family: Optional[String] = None
        self.algorithm_mode: Optional[String] = None
        self.crypto_key: Optional[String] = None
        self.maximum_key: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize CryptoServiceNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CryptoServiceNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize algorithm_family
        if self.algorithm_family is not None:
            serialized = ARObject._serialize_item(self.algorithm_family, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALGORITHM-FAMILY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize algorithm_mode
        if self.algorithm_mode is not None:
            serialized = ARObject._serialize_item(self.algorithm_mode, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALGORITHM-MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crypto_key
        if self.crypto_key is not None:
            serialized = ARObject._serialize_item(self.crypto_key, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRYPTO-KEY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize maximum_key
        if self.maximum_key is not None:
            serialized = ARObject._serialize_item(self.maximum_key, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAXIMUM-KEY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CryptoServiceNeeds":
        """Deserialize XML element to CryptoServiceNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CryptoServiceNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CryptoServiceNeeds, cls).deserialize(element)

        # Parse algorithm_family
        child = ARObject._find_child_element(element, "ALGORITHM-FAMILY")
        if child is not None:
            algorithm_family_value = child.text
            obj.algorithm_family = algorithm_family_value

        # Parse algorithm_mode
        child = ARObject._find_child_element(element, "ALGORITHM-MODE")
        if child is not None:
            algorithm_mode_value = child.text
            obj.algorithm_mode = algorithm_mode_value

        # Parse crypto_key
        child = ARObject._find_child_element(element, "CRYPTO-KEY")
        if child is not None:
            crypto_key_value = child.text
            obj.crypto_key = crypto_key_value

        # Parse maximum_key
        child = ARObject._find_child_element(element, "MAXIMUM-KEY")
        if child is not None:
            maximum_key_value = child.text
            obj.maximum_key = maximum_key_value

        return obj



class CryptoServiceNeedsBuilder:
    """Builder for CryptoServiceNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CryptoServiceNeeds = CryptoServiceNeeds()

    def build(self) -> CryptoServiceNeeds:
        """Build and return CryptoServiceNeeds object.

        Returns:
            CryptoServiceNeeds instance
        """
        # TODO: Add validation
        return self._obj
