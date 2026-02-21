"""EcucParameterDerivationFormula AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 88)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_query import (
    EcucQuery,
)


class EcucParameterDerivationFormula(ARObject):
    """AUTOSAR EcucParameterDerivationFormula."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ecuc_query_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize EcucParameterDerivationFormula."""
        super().__init__()
        self.ecuc_query_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucParameterDerivationFormula to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize ecuc_query_ref
        if self.ecuc_query_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ecuc_query_ref, "EcucQuery")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECUC-QUERY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucParameterDerivationFormula":
        """Deserialize XML element to EcucParameterDerivationFormula object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucParameterDerivationFormula object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ecuc_query_ref
        child = SerializationHelper.find_child_element(element, "ECUC-QUERY-REF")
        if child is not None:
            ecuc_query_ref_value = ARRef.deserialize(child)
            obj.ecuc_query_ref = ecuc_query_ref_value

        return obj



class EcucParameterDerivationFormulaBuilder:
    """Builder for EcucParameterDerivationFormula."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucParameterDerivationFormula = EcucParameterDerivationFormula()

    def build(self) -> EcucParameterDerivationFormula:
        """Build and return EcucParameterDerivationFormula object.

        Returns:
            EcucParameterDerivationFormula instance
        """
        # TODO: Add validation
        return self._obj
