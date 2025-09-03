#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 12:09:01 2025

@author: charter-bus
"""

# This program defines a set of reusable Python functions for performing common linear algebra operations.
# These are especially helpful for academic purposes such as checking solutions in math or physics courses.
# Each function includes comments explaining what it does and how it works.

def crossProduct(vectorA, vectorB):
    # Calculates the cross product of two 3D vectors.
    # INPUT: Two lists with 3 elements each.
    # OUTPUT: A new vector that is perpendicular to both inputs.

    newVector = [0, 0, 0]
    newVector[0] = ((vectorA[1] * vectorB[2]) - (vectorA[2] * vectorB[1]))  # X component
    newVector[1] = ((vectorA[0] * vectorB[2]) - (vectorA[2] * vectorB[0])) * -1  # Y component (flipped sign)
    newVector[2] = ((vectorA[0] * vectorB[1]) - (vectorA[1] * vectorB[0]))  # Z component
    return newVector

def vectorTripleProduct(vectorA, vectorB):
    # Calculates the dot product of two vectors (confusing name but functionally a dot product).
    # INPUT: Two lists of 3 elements.
    # OUTPUT: Scalar value representing the dot product.

    i = 0
    tripleProductSum = 0
    while i < 3:
        tripleProductSum += vectorA[i]*vectorB[i]
        i += 1
    return tripleProductSum

def verticesToVectors(vertA, vertB, vertC, vertD=[0, 0, 0]):
    # Given 3 or 4 points in 3D space, convert them into vectors based at vertA.
    # OUTPUT: Dictionary containing AB, AC, and AD vectors.

    dict = {'AB':[0, 0, 0], 'AC':[0, 0, 0], 'AD':[0, 0, 0]}
    i = 0
    vectorizedAB = []
    vectorizedAC = []
    vectorizedAD = []
    while i < 3:
        vectorizedAB.append(vertB[i] - vertA[i])
        vectorizedAC.append(vertC[i] - vertA[i])
        vectorizedAD.append(vertD[i] - vertA[i])
        i += 1
    dict['AB'] = vectorizedAB
    dict['AC'] = vectorizedAC
    dict['AD'] = vectorizedAD
    return dict

def dotProduct(vectorA, vectorB):
    # Calculates the dot product between two 3D vectors.
    # INPUT: Two 3-element lists.
    # OUTPUT: Single scalar result.

    newVector = [0, 0, 0]
    newVector[0] = (vectorA[0] * vectorB[0])
    newVector[1] = (vectorA[1] * vectorB[1])
    newVector[2] = (vectorA[2] * vectorB[2])
    dotProduct = newVector[0] + newVector[1] + newVector[2]
    return dotProduct

def InverseMatrixCofactors(matrixA):
    # Computes the adjugate (not final inverse) of a 3x3 matrix using cofactors.
    # Useful for solving systems of equations or matrix algebra.

    detMinors = [[0, 0, 0],[0, 0, 0], [0, 0, 0]]
    detMinors[0][0] = ((matrixA[1][1] * matrixA[2][2]) - (matrixA[1][2] * matrixA[2][1]))
    detMinors[0][1] = ((matrixA[1][0] * matrixA[2][2]) - (matrixA[1][2] * matrixA[2][0]))
    detMinors[0][2] = ((matrixA[1][0] * matrixA[2][1]) - (matrixA[1][1] * matrixA[2][0]))
    detMinors[1][0] = ((matrixA[0][1] * matrixA[2][2]) - (matrixA[0][2] * matrixA[2][1]))
    detMinors[1][1] = ((matrixA[0][0] * matrixA[2][2]) - (matrixA[0][2] * matrixA[2][0]))
    detMinors[1][2] = ((matrixA[0][0] * matrixA[2][1]) - (matrixA[0][1] * matrixA[2][0]))
    detMinors[2][0] = ((matrixA[0][1] * matrixA[1][2]) - (matrixA[0][2] * matrixA[1][1]))
    detMinors[2][1] = ((matrixA[0][0] * matrixA[1][2]) - (matrixA[0][2] * matrixA[1][0]))
    detMinors[2][2] = ((matrixA[0][0] * matrixA[1][1]) - (matrixA[0][1] * matrixA[1][0]))

    # Apply cofactor signs
    cofactors = [[ detMinors[0][0], -detMinors[0][1],  detMinors[0][2]],
                 [-detMinors[1][0],  detMinors[1][1], -detMinors[1][2]],
                 [ detMinors[2][0], -detMinors[2][1],  detMinors[2][2]]]

    # Transpose to get adjugate matrix
    transposedMatrix = [[cofactors[0][0], cofactors[1][0], cofactors[2][0]],
                        [cofactors[0][1], cofactors[1][1], cofactors[2][1]],
                        [cofactors[0][2], cofactors[1][2], cofactors[2][2]]]
    return transposedMatrix

def determinantOf3x3Matrix(matrixA):
    # Calculates the determinant of a 3x3 matrix using cofactor expansion.
    # INPUT: 3x3 list of lists
    # OUTPUT: Single scalar determinant

    detA = (matrixA[0][0] * ((matrixA[1][1] * matrixA[2][2]) - (matrixA[1][2] * matrixA[2][1]))) \
         - (matrixA[0][1] * ((matrixA[1][0] * matrixA[2][2]) - (matrixA[1][2] * matrixA[2][0]))) \
         + (matrixA[0][2] * ((matrixA[1][0] * matrixA[2][1]) - (matrixA[1][1] * matrixA[2][0])))
    return detA