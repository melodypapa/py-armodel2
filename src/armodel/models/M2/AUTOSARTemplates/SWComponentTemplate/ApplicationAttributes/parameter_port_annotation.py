"""ParameterPortAnnotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 158)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ApplicationAttributes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)


class ParameterPortAnnotation(GeneralAnnotation):
    """AUTOSAR ParameterPortAnnotation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    parameter_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ParameterPortAnnotation."""
        super().__init__()
        self.parameter_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ParameterPortAnnotation":
        """Deserialize XML element to ParameterPortAnnotation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ParameterPortAnnotation object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse parameter_ref
        child = ARObject._find_child_element(element, "PARAMETER")
        if child is not None:
            parameter_ref_value = ARObject._deserialize_by_tag(child, "ParameterDataPrototype")
            obj.parameter_ref = parameter_ref_value

        return obj



class ParameterPortAnnotationBuilder:
    """Builder for ParameterPortAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ParameterPortAnnotation = ParameterPortAnnotation()

    def build(self) -> ParameterPortAnnotation:
        """Build and return ParameterPortAnnotation object.

        Returns:
            ParameterPortAnnotation instance
        """
        # TODO: Add validation
        return self._obj
