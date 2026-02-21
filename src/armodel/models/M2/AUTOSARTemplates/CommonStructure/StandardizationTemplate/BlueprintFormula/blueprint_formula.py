"""BlueprintFormula AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 163)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_BlueprintFormula.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_definition_element import (
    EcucDefinitionElement,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_verbatim import (
    MultiLanguageVerbatim,
)


class BlueprintFormula(ARObject):
    """AUTOSAR BlueprintFormula."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ecuc_ref: ARRef
    verbatim: MultiLanguageVerbatim
    def __init__(self) -> None:
        """Initialize BlueprintFormula."""
        super().__init__()
        self.ecuc_ref: ARRef = None
        self.verbatim: MultiLanguageVerbatim = None

    def serialize(self) -> ET.Element:
        """Serialize BlueprintFormula to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize ecuc_ref
        if self.ecuc_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ecuc_ref, "EcucDefinitionElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECUC-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize verbatim
        if self.verbatim is not None:
            serialized = SerializationHelper.serialize_item(self.verbatim, "MultiLanguageVerbatim")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VERBATIM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BlueprintFormula":
        """Deserialize XML element to BlueprintFormula object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BlueprintFormula object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ecuc_ref
        child = SerializationHelper.find_child_element(element, "ECUC-REF")
        if child is not None:
            ecuc_ref_value = ARRef.deserialize(child)
            obj.ecuc_ref = ecuc_ref_value

        # Parse verbatim
        child = SerializationHelper.find_child_element(element, "VERBATIM")
        if child is not None:
            verbatim_value = SerializationHelper.deserialize_with_type(child, "MultiLanguageVerbatim")
            obj.verbatim = verbatim_value

        return obj



class BlueprintFormulaBuilder:
    """Builder for BlueprintFormula."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BlueprintFormula = BlueprintFormula()

    def build(self) -> BlueprintFormula:
        """Build and return BlueprintFormula object.

        Returns:
            BlueprintFormula instance
        """
        # TODO: Add validation
        return self._obj
