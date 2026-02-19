"""SignalServiceTranslationElementProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 735)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_SignalServiceTranslation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter.data_filter import (
    DataFilter,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class SignalServiceTranslationElementProps(Identifiable):
    """AUTOSAR SignalServiceTranslationElementProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    element_ref: Optional[ARRef]
    filter: Optional[DataFilter]
    transmission: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize SignalServiceTranslationElementProps."""
        super().__init__()
        self.element_ref: Optional[ARRef] = None
        self.filter: Optional[DataFilter] = None
        self.transmission: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SignalServiceTranslationElementProps":
        """Deserialize XML element to SignalServiceTranslationElementProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SignalServiceTranslationElementProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse element_ref
        child = ARObject._find_child_element(element, "ELEMENT")
        if child is not None:
            element_ref_value = ARObject._deserialize_by_tag(child, "DataPrototype")
            obj.element_ref = element_ref_value

        # Parse filter
        child = ARObject._find_child_element(element, "FILTER")
        if child is not None:
            filter_value = ARObject._deserialize_by_tag(child, "DataFilter")
            obj.filter = filter_value

        # Parse transmission
        child = ARObject._find_child_element(element, "TRANSMISSION")
        if child is not None:
            transmission_value = child.text
            obj.transmission = transmission_value

        return obj



class SignalServiceTranslationElementPropsBuilder:
    """Builder for SignalServiceTranslationElementProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SignalServiceTranslationElementProps = SignalServiceTranslationElementProps()

    def build(self) -> SignalServiceTranslationElementProps:
        """Build and return SignalServiceTranslationElementProps object.

        Returns:
            SignalServiceTranslationElementProps instance
        """
        # TODO: Add validation
        return self._obj
