"""ReferenceValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 436)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class ReferenceValueSpecification(ValueSpecification):
    """AUTOSAR ReferenceValueSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    reference_value_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ReferenceValueSpecification."""
        super().__init__()
        self.reference_value_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ReferenceValueSpecification":
        """Deserialize XML element to ReferenceValueSpecification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ReferenceValueSpecification object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ReferenceValueSpecification, cls).deserialize(element)

        # Parse reference_value_ref
        child = ARObject._find_child_element(element, "REFERENCE-VALUE")
        if child is not None:
            reference_value_ref_value = ARObject._deserialize_by_tag(child, "DataPrototype")
            obj.reference_value_ref = reference_value_ref_value

        return obj



class ReferenceValueSpecificationBuilder:
    """Builder for ReferenceValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ReferenceValueSpecification = ReferenceValueSpecification()

    def build(self) -> ReferenceValueSpecification:
        """Build and return ReferenceValueSpecification object.

        Returns:
            ReferenceValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
