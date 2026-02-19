"""EcucParameterDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 57)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 188)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_common_attributes import (
    EcucCommonAttributes,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_derivation_specification import (
    EcucDerivationSpecification,
)
from abc import ABC, abstractmethod


class EcucParameterDef(EcucCommonAttributes, ABC):
    """AUTOSAR EcucParameterDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    derivation: Optional[EcucDerivationSpecification]
    symbolic_name: Optional[Boolean]
    with_auto: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize EcucParameterDef."""
        super().__init__()
        self.derivation: Optional[EcucDerivationSpecification] = None
        self.symbolic_name: Optional[Boolean] = None
        self.with_auto: Optional[Boolean] = None
    def serialize(self) -> ET.Element:
        """Serialize EcucParameterDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucParameterDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize derivation
        if self.derivation is not None:
            serialized = ARObject._serialize_item(self.derivation, "EcucDerivationSpecification")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DERIVATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize symbolic_name
        if self.symbolic_name is not None:
            serialized = ARObject._serialize_item(self.symbolic_name, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYMBOLIC-NAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize with_auto
        if self.with_auto is not None:
            serialized = ARObject._serialize_item(self.with_auto, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WITH-AUTO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucParameterDef":
        """Deserialize XML element to EcucParameterDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucParameterDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucParameterDef, cls).deserialize(element)

        # Parse derivation
        child = ARObject._find_child_element(element, "DERIVATION")
        if child is not None:
            derivation_value = ARObject._deserialize_by_tag(child, "EcucDerivationSpecification")
            obj.derivation = derivation_value

        # Parse symbolic_name
        child = ARObject._find_child_element(element, "SYMBOLIC-NAME")
        if child is not None:
            symbolic_name_value = child.text
            obj.symbolic_name = symbolic_name_value

        # Parse with_auto
        child = ARObject._find_child_element(element, "WITH-AUTO")
        if child is not None:
            with_auto_value = child.text
            obj.with_auto = with_auto_value

        return obj



class EcucParameterDefBuilder:
    """Builder for EcucParameterDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucParameterDef = EcucParameterDef()

    def build(self) -> EcucParameterDef:
        """Build and return EcucParameterDef object.

        Returns:
            EcucParameterDef instance
        """
        # TODO: Add validation
        return self._obj
